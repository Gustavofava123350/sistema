from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from accounts.models import User_Groups, Group_Permission
from companies.models import Enterprise, Employee

class Base(APIView):
    def get_enterprise_user(self, user_id):
        enterprise = {
            "is_owner": False,
            "permission":[]
        }

        enterprise['is_owner'] = Enterprise.objects.filter(user_id=user_id).exists()

        if enterprise['is_owrner']: return enterprise

        employee = Employee.objects.filter(user_id=user_id ).first()

        if not employee: raise APIException("Este usuário não é um funcionário")

        groups = User_Groups.objects.filter(user_id=user_id).all()

        for g in groups:
            group = g.group
            permissions = Group_Permission.objects.filter(group_id=group.id).all()

        for p in permissions:
            enterprise['permissions'].append({
                "id": p.permission.id,
                 "label": p.permission.name ,
                 "codename": p.permission.codename
               })
        return enterprise
        






