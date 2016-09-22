import os
import uuid

from moviepy.editor import VideoFileClip

from django.core.files import File


class FrameCreator():
    """video_field - django file field with video file
    """

    def __init__(self, video_field):
        self.video_field = video_field

    def get_frame(self, video_frame_time='00:00:00'):
        """Get frame from video_field.
        video_frame_time - time of video frame
        Attention. Function creates tmp files in ".media/tmp/" directory.
        Tmp files are removed automatically.
        """
        frame = None
        tmp_files = []
        try:
            # create tmp video file in system to create frame
            tmp_video_path = '.media/tmp/{}'.format(self.video_field.name)
            os.makedirs(os.path.dirname(tmp_video_path), exist_ok=True)
            tmp_files.append(tmp_video_path)
            with open(tmp_video_path, 'wb+') as tmp_video_file:
                tmp_video_file.write(self.video_field.read())

            frame_extension = '.jpg'
            tmp_frame_path = tmp_video_path.split('/')
            file_name = uuid.uuid4().hex
            tmp_frame_path[-1] = '{}{}'.format(file_name, frame_extension)
            tmp_frame_path = '/'.join(tmp_frame_path)

            # create tmp video frame
            clip = VideoFileClip(tmp_video_path)
            clip.save_frame(tmp_frame_path, t=video_frame_time)
            tmp_files.append(tmp_frame_path)

            # save frame file to storage
            frame = File(open(tmp_frame_path, 'rb'))
        finally:
            # remove tmp files
            for tmp_file in tmp_files:
                os.remove(tmp_file)
        return frame
