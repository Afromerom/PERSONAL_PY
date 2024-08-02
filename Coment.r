#' @title PTC
#' @description PTC estima los padres causales de un conjunto de \code{nmR} mRNAs,
#' dado un conjunto de \code{nmiR} predictores (miRNAs). Esta estimación asume
#' un modelo lineal \deqn{Y_t = \beta X_t + \epsilon}
#' con \eqn{Y_t, X_t} los datos secuenciales del objetivo y los predictores respectivamente,
#' y \eqn{\epsilon} errores independientes e idénticamente distribuidos para los n puntos de tiempo en la serie temporal.
#' \eqn{Y_t, X_t} son los datos secuenciales obtenidos después de un análisis de pseudotiempo.
#' @usage PTC(miRNAs, mRNAs, VIM, nmiR=30, nmR=1500 , ngrid=2, alpha=0.02, complements = TRUE, explore.all=TRUE, silent=TRUE)\cr
#' @param miRNAs Una \code{matriz} que contiene la expresión génica de miRNAs.\cr
#' Se seleccionan un total de \code{nmiR} miRNAs de esta matriz para ser utilizados
#' como candidatos a predictores (es decir, padres plausibles).
#' Las columnas representan miRNAs, las filas representan muestras.
#' @param mRNAs Una \code{matriz} que contiene la expresión génica de mRNAs.\cr
#' Se seleccionan un total de \code{nmR} mRNAs de esta matriz para ser utilizados como variables de respuesta.
#' Las columnas representan mRNAs, las filas representan muestras.
#' @param VIM Expresión de VIM para ser utilizada en el cálculo de VIM_Time.
#' @param nmiR Número de miRNAs a seleccionar como candidatos a predictores.
#' @param nmR Número de mRNAs a seleccionar como variables objetivo.
#' @param ngrid Número de segmentos de los datos de series temporales utilizados para crear
#' los diferentes entornos requeridos para la prueba estadística. \code{ngrid=2} por defecto.
#' @param alpha Nivel de significancia para la prueba estadística. \code{alpha=0.02} por defecto.
#' @param complements Si \code{TRUE} (por defecto), cada entorno se compara con su complemento. Si \code{FALSE} todos los entornos se comparan por pares.
#' @param explore.all Si \code{TRUE} (por defecto), PTC explora todas las combinaciones de predictores
#' y devuelve el conjunto de todas las combinaciones que no violen la propiedad de invariancia. Si \code{FALSE}, PTC devuelve el primer conjunto que no viole la propiedad de invariancia. La exploración se realiza comenzando con el conjunto de todos los predictores y reduciendo el tamaño del conjunto eliminando un predictor a la vez.
#' @param silent Si \code{TRUE} (por defecto), PTC muestra el conjunto evaluado actualmente. Si \code{FALSE}, PTC solo muestra el número de conjuntos a explorar en la iteración actual.
#' @param TScan Una matriz de 2 columnas que contiene las relaciones miRNA-mRNA. Para un funcionamiento adecuado, los miRNAs deben estar en minúsculas y los mRNAs en mayúsculas. Si \code{NULL} (por defecto), PTC utiliza una matriz pre-cargada (archivo TScan) con TargetScan 7.0 Human.
#' @author Andres Mauricio Cifuentes_Bernal, Vu VH Pham, Xiaomei Li, Lin Liu, Jiuyong Li y Thuc Duy Le
#' @export
#' @seealso \link[PTC]{PTC.ptime}, \link[PTC]{PTC.GeneSel}, \link{TScan}, \link[PTC]{PTC.TestInvariance}.
#' @return Una \code{lista} que consiste en los siguientes elementos:
#'   \item{\code{Index}}{Una \code{lista} donde cada elemento es un mRNA objetivo.
#'    Para cada gen objetivo con al menos un padre. El índice de los padres.}
#'   \item{\code{names}}{Una \code{lista} donde cada elemento es un mRNA objetivo.
#'    Para cada gen objetivo con al menos un padre. El nombre de los padres.}
#'   \item{\code{genes}}{Los nombres de todos los genes objetivo con al menos un padre.}
#'   \item{\code{Summary}}{Una matriz que representa las interacciones reguladoras miRNA-mRNA inferidas por PTC. Las columnas de la matriz son:
#'        \enumerate{
#'           \item{\code{rank:}}{ Rango de la interacción inferida}
#'           \item{\code{miR:}}{ Nombres de los miRNAs (Padre)}
#'           \item{\code{mR:}}{ Nombres de los mRNAs (Hijo)}
#'           \item{\code{Score:}}{ Puntuación calculada por \link{PTC.RankByContext}}
#'           }
#'    }
#' @examples \dontrun{
#'    data(TCGA_BRCAdata)
#'    test1<-PTC(miRNAs=TCGA_BRCAdata$miRs, mRNAs=TCGA_BRCAdata$mRNAs, VIM=TCGA_BRCAdata$mRNAs[,"VIM"])
#' }
#' @references
#' A Pseudo-Temporal Causality Approach to Identifying miRNA-mRNA
#' Interactions During Biological Processes\cr
#' Andres M. Cifuentes-Bernal, Vu VH Pham, Xiaomei Li,
#' Lin Liu, Jiuyong Li, Thuc Duy Le \cr
#' bioRxiv 2020.07.07.192724;
#'  \url{https://doi.org/10.1101/2020.07.07.192724}
#'

PTC <- function(miRNAs, mRNAs, VIM, nmiR=30, nmR=1500, ngrid=2, alpha=0.02, complements = TRUE, explore.all=TRUE, silent=TRUE, TScan=NULL) {
  # Para compatibilidad, los nombres de mRNAs se transforman a mayúsculas
  colnames(mRNAs) <- toupper(colnames(mRNAs))

  # Cargar los datos de TS7.0_Conserved_Site_Context_Scores en el entorno actual
  data("TS7.0_Conserved_Site_Context_Scores", envir = environment())

  # Crear una lista con los datos de expresión génica de miRNAs y mRNAs
  GEData <- list(miRNAs, mRNAs)
  names(GEData) <- c("miRs", "mRNAs")

  # Ordenar los datos de expresión génica por pseudotiempo usando PTC.ptime
  seqData <- PTC.ptime(GEData, VIM)

  # Seleccionar los miRNAs y mRNAs más variables usando PTC.GeneSel
  SelData <- PTC.GeneSel(seqData, nmiR = nmiR, nmR = nmR, TScan = TScan)

  # Inicializar una lista para almacenar los resultados de PTC.TestInvariance
  PTC.outcome <- vector("list", length = length(SelData$mRs))
  names(PTC.outcome) <- SelData$mRs

  # Evaluar cada mRNA objetivo
  for (gene in SelData$mRs) {
    temp <- SelData$PParents[[gene]]
    X.TScan <- SelData$d[, temp, drop = FALSE]
    if (length(X.TScan) > 0) {
      message(paste("mRNA actual  = {", gene, "}", sep = " "))
      set.seed(1)
      PTC.outcome[gene] <- try(PTC.TestInvariance(
        Y = SelData$d[, gene, drop = FALSE],
        X = X.TScan,
        ngrid = ngrid,
        alpha = alpha,
        explore.all = explore.all,
        silent = silent,
        complements = complements
      ))
    }
  }

  # Crear una lista para almacenar los resultados finales
  Results <- list()

  # Extraer los padres causales usando Extract.Parents
  Results <- Extract.Parents(PTC.outcome, SelData$PParents)

  # Convertir la lista de interacciones en una matriz usando InterList.toMatrix
  Results$Summary <- InterList.toMatrix(Results$Names)

  # Clasificar las interacciones usando PTC.RankByContext
  Results$Summary <- PTC.RankByContext(TS7.0_Conserved_Site_Context_Scores, Results$Summary)

  # Retornar los resultados finales
  return(Results)
}
