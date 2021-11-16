from auth_example.models.account    import Account
from auth_example.models.user       import User
from rest_framework                 import serializers


class AccountSerializer(serializers.ModelSerializers):
    class Meta:
        model = Account
        fields = ['balance', 'last_change_date', 'is_active']     

    def to_representation(self, obj):#Si necesita mas Inner Join mirar el Live
        account = Account.objects.get(id=obj.id)
        user = User.objects.get(id=obj.user_id)
        return {
            'id'                : account.id,
            'balance'           : account.balance,        
            'lastChange_date'   : account.last_change_date,
            'isActive'          : account.is_active,
            'user'   : {
                'id'        : user.id, 
                'name'      : user.name,
                'email'     : user.email,
                
            }
        }

