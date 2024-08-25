from django.urls import path
from apps.orient.api.api import OrientApiView, CreateDbApiView, \
        DeleteDbApiView, CreateTableApiView, InsertTableApiView, \
        TableRowApiView, UpdateRowApiView, ListTableApiView, \
        DeleteTableApiView


urlpatterns = [
    path("connect", OrientApiView.as_view()),
    path("create/db", CreateDbApiView.as_view()),
    path("delete/db", DeleteDbApiView.as_view()),
    path("create/table", CreateTableApiView.as_view()),
    path("delete/table", DeleteTableApiView.as_view()),
    path("insert/table", InsertTableApiView.as_view()),
    path("table/row", TableRowApiView.as_view()),
    path("update/row", UpdateRowApiView.as_view()),
    path("table/list", ListTableApiView.as_view())

]