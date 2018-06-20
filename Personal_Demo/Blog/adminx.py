# coding:utf-8
import xadmin
from models import Tag, Category, Post
from xadmin import views
from form.xadminLoginForm import AdminAuthenticationForm
from xadmin.views import website

website.LoginView.login_form = AdminAuthenticationForm


class PostAdmin(object):
    list_display = ('title', 'body', 'created_time', 'modified_time', 'excerpt', 'category', 'tags', 'author')
    search_fields = ('title', 'tags', 'author')
    list_filter = ('tags',)
    list_exclude = ('id',)


class CategoryAdmin(object):
    list_display = ('name', )
    search_fields = ('name', )
    # list_filter = ('',)
    list_exclude = ('id',)


class TagAdmin(object):
    list_display = ('name', )
    search_fields = ('name', )
    # list_filter = ('',)
    list_exclude = ('id',)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "Blog Manager"
    site_footer = "Create By Zerone"


class AdminSettings(object):
    # 设置base_site.html的Title
    site_title = 'Blog Manager'
    # 设置base_site.html的Footer
    site_footer = 'Create By Zerone'
    menu_style = 'accordion'  # 'default'

    def get_site_menu(self):
        all_men = (
            {'title': 'blog', 'perm': self.get_model_perm(Post, 'view'), 'menus': (
                {'title': 'Post', 'url': self.get_model_url(Post, 'changelist'),
                 'perm': self.get_model_perm(Post, 'view')},
                {'title': 'Tags', 'url': self.get_model_url(Tag, 'changelist'),
                 'perm': self.get_model_perm(Tag, 'view')},
                {'title': 'Category', 'url': self.get_model_url(Category, 'changelist'),
                 'perm': self.get_model_perm(Category, 'view')},
            )},
        )
        return all_men


xadmin.site.register(views.CommAdminView, AdminSettings)
# xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
