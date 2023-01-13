# -*- coding: utf-8 -*-

name = 'chrome'

@early()
def version():
    import os
    return os.path.basename(os.getcwd())

variants = [
    ['platform-linux']
]

build_command = "bash {root}/install.sh {install}"

# Mikros specific
custom = {
    'description': 'Google Chrome',
    'authors': ['google'],
    'maintainers': ['google'],
    'notificationChannels': ['coreTech', 'extSoft']
}

uuid = 'repository.%s' % name

with scope("config") as config:
    config.release_packages_path = '/s/apps/packages/utils'


def pre_commands():
    import os
    user_path = "/datas/{}/tmp/.cache".format(env.USER)
    if not os.path.exists(user_path):
        os.mkdir(user_path)


def commands():
    env.CHROME_DEVEL_SANDBOX = '{root}/chrome-sandbox'
    alias('chrome', '{root}/google-chrome --password-store=basic --disk-cache-dir=/datas/$USER/tmp/.cache')

