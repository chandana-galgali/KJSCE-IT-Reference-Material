<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Scent Haven Perfume Inventory</title>
      </head>
      <body>
        <h1>Perfume Inventory</h1>
        <table border="1">
            <tr>
            <th>Name</th>
            <th>Brand</th>
            <th>Price ($)</th>
            <th>Quantity</th>
          </tr>
          <xsl:for-each select="/perfumeShop/perfume">
            <tr>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="brand"/></td>
              <td><xsl:value-of select="price"/></td>
              <td><xsl:value-of select="quantity"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
<!-- xsl file -->