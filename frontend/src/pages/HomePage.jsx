import { useState } from "react";
import { useNavigate } from "react-router-dom";
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

  return (
    <>
      <form onSubmit={changeInput}>
        <input type="email" name="email" placeholder="Email" required/>
        <input type="password" name="passwd" placeholder="Password" required/>
        <button type="button" onClick={signUpPage}>
          SignUp
        </button>
        <button>Submit</button>
      </form>
    </>
  );
}
