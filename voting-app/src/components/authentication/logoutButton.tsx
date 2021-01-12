import React from 'react';

function LogoutButton() {
  const logout = (() => {
    localStorage.removeItem('userID');
    window.location.reload();
  });

  return (
    <button type="button" onClick={logout}>Logout</button>
  );
}

export default LogoutButton;
