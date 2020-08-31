import json

from django.core.exceptions import MultipleObjectsReturned

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from verloop_app.models import Story
from verloop_app.utils import StoryUtility


class StoryView(APIView):
    """overall dashboard"""

    def post(self, request):
        """ to add words in story"""
        if len(request.data["word"].split(" "))>1:
            response_dict = {
                "error": "multiple words sent"
            }
        else:
            try:
                cur_object = Story.objects.get(offset=0)

            except MultipleObjectsReturned:
                print("Multiple stories are incomplete")

            except Exception:
                Story.objects.create(offset=0)

                cur_object = Story.objects.get(offset=0)
            if not StoryUtility.is_title_completed(cur_object):
                if cur_object.title is None:
                    cur_object.title = request.data["word"]
                    cur_object.save()
                else:
                    title = cur_object.title+" "+request.data["word"]
                    cur_object.title = " ".join(title.split(" "))
                    cur_object.save()
            elif not StoryUtility.is_sentence_completed(cur_object, request.data["word"]):
                if cur_object.sentences is None:
                    cur_object.sentences = [request.data["word"]]
                    cur_object.save()
                    StoryUtility.check_paragraph(cur_object, cur_object.sentences)
                    StoryUtility.is_story_completed(cur_object)
                else:
                    cur_object.sentences[-1] = cur_object.sentences[-1]+" "+request.data["word"]
                    cur_object.save()
                    StoryUtility.check_paragraph(cur_object, cur_object.sentences)
                    StoryUtility.is_story_completed(cur_object)
            response_dict = {
                "id": cur_object.id,
                "title": cur_object.title,
                "current_sentence": cur_object.sentences[-1]
            }

        return Response(json.dumps(response_dict), status=status.HTTP_200_OK)

