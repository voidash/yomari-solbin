import type { NextPage } from "next";
import Head from "next/head";
import { HomeView } from "../views";

const Map: NextPage = (props) => {
  return (
    <div>
      <Head>
        <title>Sol-Bin Marketplace</title>
        <meta
          name="description"
          content="Solana Scaffold"
        />
      </Head>
      <HomeView />
    </div>
  );
};

export default Map;
