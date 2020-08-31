from verloop_app.models import Story

class StoryUtility:

    @staticmethod
    def is_title_completed(current_story):
        if current_story.title is None or \
                len(current_story.title.split(" ")) < 2:
            return False
        return True

    @staticmethod
    def is_sentence_completed(current_story, word):
        if current_story.sentences is None or \
                len(current_story.sentences[-1].split(" ")) < 5:
            return False
        current_story.sentences.append(word)
        current_story.save()
        return True

    @staticmethod
    def is_para_completed(current_story):

        if current_story.paragraphs is None or \
                len(current_story.paragraphs[-1].split(",")) <= 5:
            return False
        return True

    @staticmethod
    def check_len_sentences_in_para(cur_object):

        if cur_object.paragraphs[-1] is None or len(cur_object.paragraphs[-1].split(" ")) < 5:
            print(len(cur_object.paragraphs[-1].split(" ")))
            return True
        return False

    @staticmethod
    def check_paragraph(cur_object, sentences):

        if not StoryUtility.is_para_completed(cur_object):
            if cur_object.paragraphs is None:
                cur_object.paragraphs = [sentences[-1]]
                cur_object.save()
            else:
                if StoryUtility.check_len_sentences_in_para(cur_object):
                    cur_object.paragraphs[-1] = sentences[-1]
                    cur_object.save()
                else:
                    cur_object.paragraphs.append([sentences[-1]])
                    cur_object.save()
        else:
            cur_object.paragraphs.append([sentences[-1][-1]])
            cur_object.save()

    @staticmethod
    def is_story_completed(current_story):
        if len(current_story.paragraphs) >= 7:
            current_story.offset = 1
            current_story.save()
            return True
        Story.objects.create(offset=0)
        return False