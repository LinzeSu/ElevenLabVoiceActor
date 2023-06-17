import re
from elevenlabs import Voices

class ConversationLine:
    def __init__(self, speaker, line, line_number):
        self.speaker = speaker
        self.line = line
        self.line_number = line_number

    def __str__(self):
        return f"{self.speaker}: {self.line} (Line {self.line_number})"

    def get_speaker(self):
        return self.speaker

    def get_line(self):
        return self.line

    def get_line_number(self):
        return self.line_number

def read_conversation_file(file_path):
    conversation = []

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            match = re.match(r'^(.*?):\s*(.*)$', line)

            if match:
                speaker = match.group(1)
                content = match.group(2)
                conversation.append(ConversationLine(speaker, content, line_number))

    return conversation

def find_voice_index_by_name(voices_instance: Voices, target_name: str):
    for idx, voice in enumerate(voices_instance.voices):
        if voice.name == target_name:
            return idx
    return 0  # If the voice with the target name is not found