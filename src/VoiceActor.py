import os
from elevenlabs import generate, play, set_api_key, voices, Voices, save
from ConversationLine import ConversationLine, read_conversation_file, find_voice_index_by_name

set_api_key("your_api_key")

# Get the path to the file in src/resources
current_dir = os.path.dirname(os.path.abspath(__file__))
resources_dir = os.path.join(current_dir, 'resources')
conversation_file_path = os.path.join(resources_dir, 'lines.txt')

conversation_list = read_conversation_file(conversation_file_path)
conversation_output_path = "your_output_path" + "/"

voices = voices()
print(voices)

for conversation_line in conversation_list:
    audio = generate(
        text=conversation_line.line,
        voice=voices[find_voice_index_by_name(voices, conversation_line.speaker)],
    )

    play(audio)
    save(audio, conversation_output_path + conversation_line.speaker + "_" + str(conversation_line.line_number))









