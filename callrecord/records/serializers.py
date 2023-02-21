from rest_framework import serializers
from .models import CallRecord

class CallrecordSerializer(serializers.ModelSerializer):
    """
        Serializer for CallRecord model

        Converts a CalRecord object to/from a JSON representation.
    """
    class Meta:
        model = CallRecord
        fields = '__all__'

    def validate(self, data):
        """
        Custom serializer-level validation method to ensure that phone numbers are in the range of 15 digits.
        """
        from_number = len(str(data.get('from_number')))
        to_number = len(str(data.get('to_number')))

        if from_number > 15 or to_number > 15:
            raise serializers.ValidationError('Phone numbers should be between 15 digits')
    
    