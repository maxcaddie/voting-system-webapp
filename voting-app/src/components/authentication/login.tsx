/* eslint-disable no-shadow */
import React, { useState } from 'react';
import firebase from 'firebase';
import { fireAuth } from '../../firebase';
import LogoutButton from './logoutButton';
import { localStorageUserID } from '../../constants/authenticationConstants';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  // eslint-disable-next-line no-unused-vars
  const [submitting, setSubmit] = useState(false);

  const handleSubmit = (e: any) => {
    e.preventDefault();

    setSubmit(true);

    fireAuth.signInWithEmailAndPassword(email, password).then((e: firebase.auth.UserCredential) => {
      if (e.user) {
        localStorage.setItem(localStorageUserID, e.user.uid);
        alert(`Log in successful ${localStorage.getItem(localStorageUserID)}`);
        window.location.reload();
        // return history.push(`/${e.user.uid}/Home`);
      }
    }).catch((error) => {
      // eslint-disable-next-line no-alert
      alert(error);
      setSubmit(false);
    });
  };

  return (
    <div style={{ marginTop: '50px', marginLeft: '30%', marginRight: '30%' }}>
      <form
        style={{ display: 'flex', flexDirection: 'column' }}
        onSubmit={handleSubmit}
      >
        <p>abc@potus.com</p>
        <input type="text" onChange={(e) => { setEmail(e.target.value); }} />
        <p>123456</p>
        <input type="password" onChange={(e) => { setPassword(e.target.value); }} />
        <input type="submit" />
      </form>
      <LogoutButton />
    </div>
  );
}

export default LoginForm;
