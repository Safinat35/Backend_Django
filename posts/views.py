from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .model import predict
import json

@csrf_exempt
def classify_text(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("text", "")
            result = predict(text)
            return JsonResponse(result)
        except Exception as e:
            print("🔥 Internal Server Error:", e)  # Add this line
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST allowed"}, status=405)
