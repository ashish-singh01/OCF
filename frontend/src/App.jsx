import { BrowserRouter, Route, Routes } from "react-router-dom";

import "./App.css";
import HomePage from "./pages/HomePage";
import SignUp from "./pages/SignUp";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<HomePage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/signup" element={<SignUp/>}/>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
