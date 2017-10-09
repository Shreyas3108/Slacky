from django.core.exceptions import ValidationError
# Create your models heredef validate_content(value):
def validate_content(value):
	content = value
	if(content ==""):
		raise ValidationError("Cannot be empty")
	return value