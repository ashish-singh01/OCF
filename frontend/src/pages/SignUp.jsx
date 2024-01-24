import { useNavigate } from "react-router-dom";

export default function SignUp() {
  const navigate = useNavigate();

  async function changeInput(event) {
    event.preventDefault();
    const fd = new FormData(event.target);
    const data = Object.fromEntries(fd.entries());
    if (data.passwd !== data.conPasswd) {
      alert("Password Mismatch");
    }else{
      // console.log(data);
      try {
        await fetch("http://127.0.0.1:5000/register", {
          method: "POST",
          body: fd,
          mode: "no-cors"
        });
      } catch (error) {
        console.error(error);
      }
    }
  }

  return (
    <>
      <form onSubmit={changeInput}>
        <input type="text" name="name" placeholder="Name" required />
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="passwd" placeholder="Password" required />
        <input
          type="password"
          name="conPasswd"
          placeholder="Confirm Password"
          required
        />
        <button>Submit</button>
        <button
          type="button"
          onClick={() => {
            navigate("/home");
          }}
        >
          Go Back
        </button>
      </form>
    </>
  );
}
