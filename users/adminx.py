import xadmin

from users.models import UserProfile


class UserAdmin(object):

    list_display = ['name', 'gender', 'mobile', 'birthday', 'email']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserAdmin)