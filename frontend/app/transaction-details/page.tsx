"use client";
import React, { use, useEffect, useState } from "react";
import axios from "axios";

const TransactionDetailsPage = () => {
  const [cart, setCart] = useState<any[]>([]);
  const [totalPrice, setTotalPrice] = useState<number>(0);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/transaction-details/")
      .then((response) => {
        setCart(response.data)
        const total_price = response.data.reduce(
            (total:any, trans:any) => total + trans.quantity * trans.price,
            0
        );
        setTotalPrice(total_price);
      })
      .catch((error) => console.log(error));
  }, []);

  const handleCheckout = () => {
    console.log("Checkout button clicked");
    axios
      .post(
        "http://127.0.0.1:5000/transaction/",
        { total_price: totalPrice },
        { headers: { "Content-Type": "application/json" } }
      )
      .then((response) => {
        // Handle successful response
        console.log("Transaction successful");
      })
      .catch((error) => {
        // Handle error
        console.log("Transaction failed");
      });
  };

  return (
    <div>
      <h1>Transaction Details</h1>
      <h2>Cart:</h2>
      {cart.map((trans) => (
        <div key={trans.transaction_detail_id}>
          <p>Transaction Detail ID: {trans.transaction_detail_id}</p>
          <p>Product ID: {trans.product_id}</p>
          <p>Price: {trans.price}</p>
          <p>Quantity: {trans.quantity}</p>
          <p>User ID: {trans.user_id}</p>
          <p>Transaction ID: {trans.transaction_id}</p>
        </div>
      ))}
        <p>Total Price: {totalPrice}</p>
      <button onClick={handleCheckout}>Checkout</button>
    </div>
  );
};

export default TransactionDetailsPage;
