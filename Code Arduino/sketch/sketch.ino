///////////////////////////////////////////////////////////////////////////////// ANNEXE A ENLEVER DU FICHIER /////////////////////////////////////////////////////////////////////////////////
const int pinMesure = A0;
const int pinGenerateur = 8;

// Initialise certaines valeurs variables pour gain de temps :
int commandePortSerie;
int valeur_mesure;

float releve_valeur() {
  valeur_mesure = analogRead(pinMesure);
  return(valeur_mesure);
}

void envoi_mesure(int valeur_mesure) {
  Serial.print(millis());
  Serial.print(";");
  Serial.print(valeur_mesure);
}

// From https://www.arduino.cc/en/Tutorial/BuiltInExamples/SerialCallResponse
void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  
  pinMode(pinGenerateur, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.print("\n");

  establishContact();  // send a byte to establish contact until receiver responds
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}

int recoit_commande() {
  return(char(Serial.read()) - '0');
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Commandes possibles pour l'Arduino :
const int GENERATEUR_ON = 0;
const int GENERATEUR_OFF = 1;
const int RELEVE_VALEUR = 2;

void loop() {
  if (Serial.available() > 0) {
    
    int commandePortSerie = recoit_commande(); // Réception d'une commande
    
    switch (commandePortSerie) {

      case GENERATEUR_ON :
        digitalWrite(LED_BUILTIN, HIGH);   // Allume la LED
        digitalWrite(pinGenerateur, HIGH); // Allume le générateur
        Serial.print("\n");
        break;

      case GENERATEUR_OFF:
        digitalWrite(LED_BUILTIN, LOW);    // Éteint la LED
        digitalWrite(pinGenerateur, LOW);  // Éteint le générateur
        Serial.print("\n");
        break;

      case RELEVE_VALEUR :
        valeur_mesure=releve_valeur();
        envoi_mesure(valeur_mesure);
        Serial.print("\n");
        break;
//
//      case default :
//        Serial.print("\n");
//        break;
    }
  }
}
