import React from 'react';

function CsvUploader() {
  return (
    <form action="/uploader" method="POST" encType="multipart/form-data">
      <input type="file" name="file" />
      <input type="submit" />
    </form>
  );
}

export default CsvUploader;
