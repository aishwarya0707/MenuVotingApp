from rest_framework import serializers

from users.models import Employee

from .models import Menu, Restaurant, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializer for the Restaurant model.
    """

    class Meta:
        model = Restaurant 
        fields = "__all__" 


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for the Menu model.
    """

    class Meta:
        model = Menu 
        fields = [
            "id",
            "restaurant",
            "items",
            "date",
        ]


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vote model.
    """

    class Meta:
        model = Vote
        fields = ["menu", "employee", "points"]


class VoteRequestSerializer(serializers.Serializer):
    """
    Serializer for handling vote requests, including validation for multiple menu votes.
    """

    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all()
    )  # Validate employee ID against Employee model.

    menuItems = Menu.objects.all()
    menu_1 = serializers.PrimaryKeyRelatedField(queryset=menuItems)
    menu_2 = serializers.PrimaryKeyRelatedField(queryset=menuItems)
    menu_3 = serializers.PrimaryKeyRelatedField(queryset=menuItems)

    def validate(self, data):
        """
        Custom validation for ensuring that all menu choices are unique.
        """
        menu_1, menu_2, menu_3 = data["menu_1"], data["menu_2"], data["menu_3"]

        # Ensure all menu choices are unique
        if len({menu_1, menu_2, menu_3}) != 3:
            raise serializers.ValidationError(
                "Menus must be unique."
            )  # Raise an error if duplicate menus are found.

        return data
