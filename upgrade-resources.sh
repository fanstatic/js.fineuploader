#!/usr/bin/env sh

if [ -d node_modules ]; then
  rm -rf node_modules
fi

npm install fine-uploader

rm -rf js/fineuploader/resources/*
mv node_modules/fine-uploader/fine-uploader js/fineuploader/resources/
mv node_modules/fine-uploader/jquery.fine-uploader js/fineuploader/resources/
rm -rf node_modules
