import 'firebase/auth';
import firebase from 'firebase/app';
import firebaseConfig from './firebaseapikey';

// Your web app's Firebase configuration

const firebaseApp = firebase.initializeApp(firebaseConfig);

export const firestore = firebaseApp.firestore();

export const fireAuth = firebaseApp.auth();

export default firebaseApp;
