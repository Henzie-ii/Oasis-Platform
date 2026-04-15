DATABASE ={
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'DB_HOST',
        'PORT': 'DB_PORT',
        'OPTIONS':{
            'init_command': 'SET sql_mode= STRICT_TRANS_TABLES',
            'charset': 'utf8mb4'
        }
    }
}