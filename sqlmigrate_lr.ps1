param
(
    [string]
    $AppName
)
py .\manage.py sqlmigrate $AppName 0001
