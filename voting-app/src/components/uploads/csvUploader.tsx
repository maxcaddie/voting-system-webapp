import React from 'react';
import { localStorageUserID } from '../../constants/authenticationConstants';

function CsvUploader() {
  const getUserId = (() => localStorage.getItem(localStorageUserID));

  return (
    <form action={`/uploader/${getUserId()}`} method="POST" encType="multipart/form-data">
      <input type="file" name="file" />
      <input type="submit" />
    </form>
  );
}

export default CsvUploader;
