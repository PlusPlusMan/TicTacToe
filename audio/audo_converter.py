"""
Converts audio files to a format that can be used in pygame.mixer
"""

from pydub import AudioSegment
from glob import glob
def convert_audio(input_file, output_file, sample_rate, bit_depth):
    sound = AudioSegment.from_file(input_file, format=".wav")
    sound = sound.set_frame_rate(sample_rate)
    sound = sound.set_sample_width(bit_depth // 8)
    sound.export(output_file, format="wav")

# audio_list = []
# for i in glob("*.wav"):
#     input_file = f"{i}"
#     output_file = f"{i}"
#     sample_rate = 44100
#     bit_depth = 16
#     convert_audio(input_file, output_file, sample_rate, bit_depth)

input_file = r"cr.wav"
output_file = r"cr.wav"
sample_rate = 44100
bit_depth = 16
convert_audio(input_file, output_file, sample_rate, bit_depth)
