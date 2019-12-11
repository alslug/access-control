# access-control

Et setup til at kontrollere adgangen til vores lokale.

Nøgle-data ligger ikke ved døren, men adgangs-tilladelse hentes via et https-kald fra vores medlemskartotek.

Af sikkerheds-hensyn bør en skannede kode hashes, inden den sendes til backenden, så den ikke ligger synligt.

KODE er den skannede kode fra RFID-læseren

SENDT_KODE = sha512 ( sha512 ( KODE + "!" + DEVICE-SALT ) + "!" + ENGANGS-SALT )

