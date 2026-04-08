import Home from './home'
import Login from './login'
import Splash from "./splash";
import { createBrowserRouter,RouterProvider } from 'react-router-dom';
function App() {

  const router=createBrowserRouter([
    {
      path:'/',
      element:<Splash/>
    },
    {
      path:'/home',
      element:<Home/>
    },
    {
    path:'/login',
    element:<Login/>
  }])
  return (
    <>
    <RouterProvider router={router}/>
    </>
  );
}

export default App
