import { useState } from "react";
import { redirect, useNavigate } from "react-router-dom";
import SignUp from "./SignUp";

export default function Login() {
  let username = "";

  const navigate = useNavigate();
  // function changeInput(event) {
  //   event.preventDefault();
  //   const fd = new FormData(event.target);
  //   const data = Object.fromEntries(fd.entries());
  //   console.log(data);
  // }

  async function login(event) {
    event.preventDefault();
    const fd = new FormData(event.target);
    const data = Object.fromEntries(fd.entries());
    try {
      await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        body: fd,
      })
        .then((response) => {
          if (response.status == 200) {
            username = response.json();
            // console.log(username);
            return username;
            //navigate("/home/username", { state: { data: username } });
          }
        })
        .then((userdata) => {
          // console.log(userdata.message);
          navigate("/home", { state: { data: userdata.message } });
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
        <button type="button" onClick={() => navigate("/signup")}>
          SignUp
        </button>
      </form>
    </>
  );
}
