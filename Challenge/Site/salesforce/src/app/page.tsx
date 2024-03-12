import Header from "./components/header";
import styles from "./page.module.css";
import Inicio from "./components/inicio";
import Produtos from "./components/produtos";
import Beneficios from "./components/beneficios";
import Costumer360 from "./components/costumer360";
import ProvaSocial from "./components/provaSocial";
import Footer from "./components/footer";


export default function Home() {
  return (
    <main className={styles.main}>
      <Header />
      <Inicio />
      <Produtos />
      <Beneficios />
      <Costumer360 />
      <ProvaSocial />
      <Footer />
    </main>

  );
}
