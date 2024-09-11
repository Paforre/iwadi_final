from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas import Parcours, Form, NiveauEtude
from service import generateParcours
from agents import generateParcours

search_route = APIRouter(prefix="/parcours")
searchTags = "Recherche de Parcours"


@search_route.post('/', response_model=List[Parcours], tags=[searchTags])
async def get_parcours(form: Form):
    """
    Function for getting the response from Agent AI

    Args (Form): the entry request with user data

    Returns (JSON): a list of objects withe the proposed paths
    """
    MESSAGE_BACHELOR_OBLIGATOIRE = ("La passion et les matières sont "
                                    "obligatoires pour un bachelier")

    MESSAGE_POSTBAC_OBLIGATOIRE = ("La spécialité et le niveau d'étude sont "
                                   "obligatoires pour un pos-bachelier")

    if form.niveau_etude == NiveauEtude.BAC and (
        form.passions is None or form.matieres is None
            ):
        raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"{MESSAGE_BACHELOR_OBLIGATOIRE}",
                )
    if form.niveau_etude in [
        NiveauEtude.LICENCE,
        NiveauEtude.MASTER,
        NiveauEtude.DOCTORAT
    ] and (form.specialite is None or form.metier is None):
        raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"{MESSAGE_POSTBAC_OBLIGATOIRE}",
        )

    return generateParcours(**form.model_dump())
