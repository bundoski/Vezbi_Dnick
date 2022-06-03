from django.contrib import admin
# from rangefilter.filters import DateTimeRangeFilter
from datetime import datetime

# Register your models here.
from .models import Post, Profile, Block, Comment


class CommentAdmin(admin.TabularInline):
    model = Comment
    extra = 0
    list_display = ("content",)

    def save_model(self, request, obj, form, change):
        obj.comment_author = Profile.objects.filter(user=request.user).first()
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return []
        elif request.user == obj.author.user:
            return ['comment_author']
        else:
            return ['content', 'comment_author']


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    list_display = ("title", "author")
    search_fields = ("title", "content")
    # list_filter = (("date_created", DateTimeRangeFilter),)

    # za avtomatsko dodavanje na author, date_created i last_modified
    def save_model(self,request, obj, form, change):
        obj.author = Profile.objects.filter(user=request.user).first()
        if obj.date_created == None:
            obj.date_created = datetime.now()
        obj.last_modified = datetime.now()
        super().save_model(request, obj, form, change)

    # tie korisnici shto ne se blokirani od avtorot, smeat da gi gledaat negovite postovi
    def has_view_permission(self, request, obj=None):
        if obj == None:
            return True
        post_author=Profile.objects.filter(user=obj.author).first()
        user_profile=Profile.objects.filter(user=request.user).first()
        blocked_users=Block.objects.filter(blocker=post_author).all()
        return not blocked_users.filter(blocked=user_profile).exists()

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ['date_created', 'last_modified', 'author']
        elif request.user == obj.author.user:
            return ['date_created', 'last_modified', 'author']
        else:
            return ['title', 'author', 'content', 'date_created', 'last_modified']
admin.site.register(Post, PostAdmin)


class BlockAdmin(admin.StackedInline):
    model = Block
    extra = 0
    fk_name = 'blocker'
    def has_add_permission(self, request, obj=None):
        if obj == None:
            return False
        return request.user == obj.user


class ProfileAdmin(admin.ModelAdmin):
    inlines=[BlockAdmin]
    list_display = ("first_name", "last_name", "user")
    # site korisnici mozat da gi gledaat profilite na site drugi korisnici
    def has_view_permission(self, request, obj=None):
        return True

    # samo adminot smee da dodava novi profili
    def has_add_permission(self, request):
        return request.user.is_superuser

    # korisnikot moze da go promeni samo svojot profil
    def has_change_permission(self, request, obj=None):
        if obj == None:
            return False
        return request.user == obj.user

    # korisnikot moze da go izbrisi samo svojot profil
    def has_delete_permission(self, request, obj=None):
        if obj == None:
            return False
        return request.user.is_superuser or request.user == obj.user
admin.site.register(Profile, ProfileAdmin)







