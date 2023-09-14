import React from 'react';
import logo from '/Users/yashshah/Desktop/Rutgers-Foodies/src/assets/rutgerslogo.jpg';

export const Heading = () => {
  return (
    <div className="text-center">
      <img src={logo} alt="Rutgers Foodies Logo" className="mx-auto" />
      Rutgers Foodies
    </div>
  );
};

export default Heading;