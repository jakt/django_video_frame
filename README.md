# Django video frame
====================

Create frame from video file using django model field.

## Install

+ download repository
+ enter to main directory
+ run command: ```python setup.py install```

Or just copy core.py file and use source code. Don't forget about requirements.

## How to use

```
...
from django_video_frame.core import FrameCreator

MyModel(models.Model):
    file = models.FileField(...)
    video_frame = models.ImageField(...)
    ...

    def save(self, *args, **kwargs):
        frame_creator = FrameCreator(video_field=self.file)
        # video_frame_time is not required
        self.video_frame = frame_creator.get_frame(video_frame_time='00:00:15')
        super().save(*args, **kwargs)
```
