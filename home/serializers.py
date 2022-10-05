import shutil
from rest_framework import serializers
from .models import *

class FileListSerializer(serializers.serializer):
    files = serializers.ListField(
        child = serializers.FileField(max_length = 10000000, allow_empty_file= False, use_url = False)
    )
 
    def zip_files(folder):
        shutil.make_archive(folder, 'zip', folder)

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder = folder, file = file)
            files_objs.append(files_obj)

        self.zip_files(folder.uid)

        return {'files':{}, 'folder': str(folder.uid)}


    