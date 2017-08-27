

broker_url = 'pyamqp://guest@localhost//'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True

imports = (
    'cyanic.user.tasks',
)
