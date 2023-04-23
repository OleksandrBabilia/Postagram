import { useNavigate } from "react-router-dom";
import axiosService from "../helpers/axios";
import axios from "axios";

function useUserActions() {
  const navigate = useNavigate();
  const baseURL = process.env.REACT_APP_API_URL;

  return {
    login,
    register,
    logout,
    edit,
  };

  function login(data) {
    return axios.post(`${baseURL}/auth/login/`, data).then((res) => {
      setUserData(res.data);
      navigate("/");
    });
  }

  function register(data) {
    return axios.post(`${baseURL}/auth/register/`, data).then((res) => {
      setUserData(res.data);
      navigate("/");
    });
  }

  function edit(data, userId) {
    return axiosService
      .patch(`${baseURL}/user/${userId}/`, data, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((res) => {
        localStorage.setItem(
          "auth",
          JSON.stringify({
            access: getAccessToken(),
            refresh: getRefreshToken(),
            user: res.data,
          })
        );
      });
  }

  function logout() {
    localStorage.removeItem("auth");
    navigate("/login");
  }
}

function getUser() {
  const auth = JSON.parse(localStorage.getItem("auth")) || null;
  if (auth) {
    return auth.user;
  } else {
    return null;
  }
}

function getAccessToken() {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth.access;
}

function getRefreshToken() {
  const auth = JSON.parse(localStorage.getItem("auth"));
  return auth.refresh;
}

function setUserData(data) {
  localStorage.setItem(
    "auth",
    JSON.stringify({
      access: data.access,
      refresh: data.refresh,
      user: data.user,
    })
  );
}

export {
  useUserActions,
  getUser,
  getAccessToken,
  getRefreshToken,
  setUserData,
};