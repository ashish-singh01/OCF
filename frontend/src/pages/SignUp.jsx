import { useNavigate } from "react-router-dom";

export default function SignUp() {
  const navigate = useNavigate();

  function changeInput(event) {
    event.preventDefault();
    const fd = new FormData(event.target);
    const data = Object.fromEntries(fd.entries());
    console.log(data);
  }

  return (
    <>
      <form onSubmit={changeInput}>
        <input type="text" name="name" placeholder="Name" required/>
        <input type="email" name="email" placeholder="Email" required/>
        <input type="password" name="passwd" placeholder="Password" required />
        <input type="password" name="conPasswd" placeholder="Confirm Password" required/>
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
