<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>Choix des spé de 1er</title>
</head>
<body>
    <div class="card text-center">
        <div class="card-header">
          <ul class="nav nav-tabs card-header-tabs">
            <li class="nav-item">
              <a class="nav-link active" aria-current="true" href="#">Choix des spécialités</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Traitement</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Rien</a>
            </li>
          </ul>
        </div>
        <div class="card-body">
          <h5 class="card-title">Choix des spécialités de Premières</h5>
            <div>
                <form action=<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?> method="post" enctype="multipart/form-data">
                    <table style="width: 100%;">
												<tr>
														<td>Nom</td>
														<td><input type="text" name="name" id=""></td>
														<td id="name_"></td>
												</tr>
												<tr>
														<td>Genre</td>
														<td>Masculin 
																<input type="radio" name="genre" id="" value="Masculin">
																Féminin
																<input type="radio" name="genre" id="" value="Féminin">
														</td>
														<td id="genre_">
														</td>
												</tr>
												<tr>
													<td><br></td>
												</tr>
                        <tr>
                            <td>
                                <p>1 choix de spé</p>
                            </td>
                            <td>
                                <p>2 choix de spé</p>
                            </td>
                            <td>
                                <p>3 choix de spé</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <select class="form-select" aria-label="1 choix de spécialités" id="first-choice" name="spe1" size="3">
                                <option selected>Choisir une option</option>
                                <option value="Maths">Maths</option>
                                <option value="SP">SP</option>
                                <option value="NSI">NSI</option>
                                <option value="SI">SI</option>
                                <option value="HG">HG</option>
                                <option value="SVT">SVT</option>
                                <option value="Langues">Langues</option>
                                <option value="Littérature">Littérature</option>
                            </select>
                            </td>
                            <td>
                                <select class="form-select" aria-label="2 choix de spécialités" id="second-choice" name="spe2" size="3">
                                    <option selected>Choisir une option</option>
                                    <option value="Maths">Maths</option>
                                    <option value="SP">SP</option>
                                    <option value="NSI">NSI</option>
                                    <option value="SI">SI</option>
                                    <option value="HG">HG</option>
                                    <option value="SVT">SVT</option>
                                    <option value="Langues">Langues</option>
                                    <option value="Littérature">Littérature</option>
                                </select>
                            </td>
                            <td>
                                <select class="form-select" aria-label="3 choix de spécialités" id="third-choice" name="spe3" size="3">
                                    <option selected>Choisir une option</option>
                                    <option value="Maths">Maths</option>
                                    <option value="SP">SP</option>
                                    <option value="NSI">NSI</option>
                                    <option value="SI">SI</option>
                                    <option value="HG">HG</option>
                                    <option value="SVT">SVT</option>
                                    <option value="Langues">Langues</option>
                                    <option value="Littérature">Littérature</option>
                                </select>
                            </td>
                        </tr>
												<tr>
													<td id="spe1_"></td>
													<td id="spe2_"></td>
													<td id="spe3_"></td>
												</tr>
                        
                    </table>
                    <input type="submit" value="Validation" class="btn btn-primary m-3">
                </form>
            </div>
        </div>
      </div>
			<script src="script.js"></script>
			<?php
			$name = $_POST["name"];
			$genre = $_POST["genre"];
			$spe1 = $_POST["spe1"];
			$spe2 = $_POST["spe2"];
			$spe3 = $_POST["spe3"];
    if (empty($name) 
		or empty($genre) 
		or $spe1 == "Choisir une option"
		or $spe2 == "Choisir une option"
		or $spe3 == "Choisir une option") {
						if (empty($name)){
							echo '<script> check_form(\'name_\')</script>';
						}
						if (empty($genre)){
							echo '<script> check_form(\'genre_\')</script>';
						}
						if ($spe1 == "Choisir une option"){
							echo '<script> check_form(\'spe1_\')</script>';
						}
						if ($spe2 == "Choisir une option"){
							echo '<script> check_form(\'spe2_\')</script>';
						}
						if ($spe3 == "Choisir une option"){
							echo '<script> check_form(\'spe3_\')</script>';
						}
		// TEST pour savoir si le formulaire a été bien rempli
				} else {
						echo "<h2 style='text-align: center'> <u> * Les INFORMATIONS FOURNIES sont : *</u> </h2>";
					echo ("<p> <b> Votre nom est:</b> ".$name."</p>");
					echo ("<p> <b> Votre genre est:</b> ".$genre."</p>");
					echo ("<p> <b> Votre 1er spécialités est:</b> ".$spe1."</p>");
					echo ("<p> <b> Votre 2e spécialités est:</b> ".$spe2."</p>");
					echo ("<p> <b> Votre 3e spécialités est:</b> ".$spe3."</p>");
					$file_open = fopen("fichier_data5.csv", "a");
// Ouverture du fichier CSV, "a" veut dire qu'on va faire un append.
// On prépare les données à mettre dans le fichier csv en "array".
        $form_data = array(
            'name' => $name,
            'genre' => $genre,
            'spe1' => $spe1,
            'spe2' => $spe2,
            'spe3' => $spe3,
        );
// Attention fputcsv() attend un "array" comme second paramètre pas un string.
        fputcsv($file_open, $form_data);
// Remise à 0 des variables pour une nouvelle saisie.
        $name = '';
        $spe3 = '';
        $genre = '';
        $spe1 = '';
        $spe2 = '';
					echo "<h2 style='text-align: center;color:green;'> <u> * Vos données sont ENREGISTREES *</u> </h2>";
				}
   
?>   
</body>
</html>