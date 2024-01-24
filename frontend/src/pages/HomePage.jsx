import { useState } from "react";
import { redirect, useNavigate } from "react-router-dom";
import SignUp from "./SignUp";

export default function HomePage() {
  const navigate = useNavigate();
  function changeInput(event) {
    event.preventDefault();
    const fd = new FormData(event.target);
    const data = Object.fromEntries(fd.entries());
    console.log(data);
  }

  function signUpPage() {
    navigate("/signup");
  }
  async function login(event) {
    event.preventDefault();
    const fd = new FormData(event.target);
    const data = Object.fromEntries(fd.entries());
    try {
      await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        body: fd,
        mode: "no-cors",
      }).then((response) => {
        if (response.status == 200) {
          console.log("Login Sucess");
        }
      });
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <>
      <form onSubmit={login}>
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="passwd" placeholder="Password" required />
        <button>Submit</button>
        <button type="button" onClick={signUpPage}>
          SignUp
        </button>
      </form>
    </>
  );
}
