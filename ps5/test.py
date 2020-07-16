from datetime import timedelta, datetime
import string

class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):
        #Remove punctuation
        cleantext = "".join([char if char not in string.punctuation else " " for char in text.lower()])
        cleanphrase = "".join([char if char not in string.punctuation else " " for char in self.phrase.lower()])
        print(cleantext)
        print(cleanphrase)
        #Remove spaces in text
        nospacetext = " ".join(cleantext.split()) + " "
        print(nospacetext)
        #Remove spaces in phrase
        nospacephrase = " ".join(cleanphrase.split()) + " "
        print(nospacephrase)
        if nospacephrase in nospacetext:
            return True
        else:
            return False


class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())


symbols = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
s1 = TitleTrigger("purple cow")
print(s1.evaluate(symbols))
print(s1.evaluate(exclaim))