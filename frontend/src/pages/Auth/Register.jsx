import React, { useState } from "react";
import axios from "axios";
import Swal from "sweetalert2"; // Import SweetAlert2
import useUserStore from "../../store/userStore";
import { useNavigate } from "react-router";

const Register = () => {
  const [isSignUp, setIsSignUp] = useState(false); // State to toggle between Sign In and Sign Up
  const { setUser } = useUserStore();
  const navigate = useNavigate();

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    const fd = new FormData(e.target);
    const data = Object.fromEntries(fd.entries());

    try {
      if (isSignUp) {
        const response = await axios.post("http://127.0.0.1:8000/user", data);
        Swal.fire({
          icon: "success",
          title: "Registration Successful",
          text: "You have successfully signed up!",
        });

        setIsSignUp(false);
      } else {
        const response = await axios.post(
          `http://127.0.0.1:8000/user/signin`,
          data
        );
        Swal.fire({
          icon: "success",
          title: "Login Successful",
          text: "Welcome back!",
        });

        setUser(response.data);
        navigate("/dashboard");
      }
    } catch (error) {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: error.response?.data?.message || "Something went wrong!",
      });
      console.error(`Error: ${error}`);
    }
  };

  return (
    <div className="flex h-full">
      {/* Left Side */}
      <div className="w-2/3 flex items-center justify-center bg-[url('/smile.jpg')] bg-no-repeat bg-cover bg-center"></div>

      {/* Right Side */}
      <div className="w-1/3 flex flex-col items-center justify-center p-8">
        <form
          onSubmit={handleFormSubmit}
          className="w-full max-w-sm h-full flex flex-col items-center justify-center"
        >
          <h1 className="text-4xl my-4 font-bold text-center">
            {isSignUp ? "Sign Up" : "Sign In"}
          </h1>
          {/* Additional Field for Sign Up */}
          {isSignUp && (
            <input
              type="text"
              name="cname"
              required
              placeholder="Company Name"
              className="w-full p-2 my-2 rounded-lg border border-gray-300"
            />
          )}
          {/* Common Input Fields */}
          <input
            type="email"
            name="email"
            required
            placeholder="Email"
            className="w-full p-2 my-2 rounded-lg border border-gray-300"
          />
          <input
            type="password"
            name="password"
            required
            placeholder="Password"
            className="w-full p-2 my-2 rounded-lg border border-gray-300"
          />
          {/* Submit Button */}
          <button
            type="submit"
            className="bg-[#093649] w-full py-2 my-4 text-white font-bold rounded-lg hover:bg-[#3f4f55]"
          >
            {isSignUp ? "Sign Up" : "Sign In"}
          </button>

          <button
            type="button"
            onClick={() => setIsSignUp(!isSignUp)}
            className="text-blue-400 underline hover:cursor-pointer hover:text-blue-600"
          >
            {isSignUp
              ? "Already have an account? Sign In"
              : "Don't have an account? Sign Up"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;
