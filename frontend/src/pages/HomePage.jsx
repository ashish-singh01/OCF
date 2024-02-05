import { useLocation } from "react-router-dom";

export default function HomePage() {
  const location = useLocation()
  const {data} = location.state || {}


  return (
    <>
      <h1>Welcome {data}</h1>
    </>
  );
}
