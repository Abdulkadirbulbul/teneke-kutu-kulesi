using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;

public class mDrag : MonoBehaviour, IDragHandler, IBeginDragHandler, IEndDragHandler
{

    private RectTransform rectTransform;
    private float speed = 1.8f;
    private void Start()
    {
        rectTransform = GetComponent<RectTransform>();
    }
    public void OnBeginDrag(PointerEventData eventData)
    {
    
    }

    public void OnDrag(PointerEventData eventData)
    {
        //transform.position = Input.mousePosition;
        rectTransform.anchoredPosition += eventData.delta * speed ;
 
    }

    public void OnEndDrag(PointerEventData eventData)
    {
   
    }
}
