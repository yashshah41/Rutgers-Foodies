import React from 'react';
import logo from '../assets/rutgerslogo.png';

export const Heading = () => {
  return (
    <div className="bg-red-500 text-white text-center py-20 flex items-center justify-center">
      <img src={logo} alt="Rutgers Foodies Logo" className="w-32 h-32 mx-4" />
      <div className="text-4xl font-semibold font-serif">utgers Foodies</div>
    </div>
  );
};

export default Heading;
