# NX 1872
# Journal created by Admin on Fri Jun 14 14:54:36 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId1, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 27.172520967809469, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys1 = workPart.Features.FindObject("SKETCH(1:1B)")
    point1 = datumCsys1.FindObject("POINT 1")
    geom2_1.Geometry = point1
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = arc1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(0.0, 3.3447432068735701, 0.0)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension1 = sketchDimensionalConstraint1.AssociatedDimension
    
    expression1 = sketchDimensionalConstraint1.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId2, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 14.624968808145205, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = arc2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = arc1
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = arc2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(0.0, 3.3447432068735701, 0.0)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension2 = sketchDimensionalConstraint2.AssociatedDimension
    
    expression2 = sketchDimensionalConstraint2.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->草圖約束(K)->尺寸(D)->快速(P)...
    # ----------------------------------------------
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines5 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines8)
    
    theSession.SetUndoMarkName(markId3, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits1 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits2 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits3 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits4 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits5 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits6 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits7 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits8 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits9 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits10 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits11 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits12 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits13 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits14 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits15 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits16 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits17 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits18 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits19 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits20 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    point1_1 = NXOpen.Point3d(5.165408584019251, 26.677039751557622, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.DrfTangent, arc1, workPart.ModelingViews.WorkView, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(5.165408584019251, 26.677039751557622, 0.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc1, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    point1_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    dimensionlinearunits21 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits23 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin1 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin1.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin1.View = NXOpen.View.Null
    assocOrigin1.ViewOfGeometry = workPart.ModelingViews.WorkView
    point2 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point2
    assocOrigin1.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.DimensionLine = 0
    assocOrigin1.AssociatedView = NXOpen.View.Null
    assocOrigin1.AssociatedPoint = NXOpen.Point.Null
    assocOrigin1.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.XOffsetFactor = 0.0
    assocOrigin1.YOffsetFactor = 0.0
    assocOrigin1.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder1.Origin.SetAssociativeOrigin(assocOrigin1)
    
    point3 = NXOpen.Point3d(17.109290598493534, 43.068214265173395, 0.0)
    sketchRapidDimensionBuilder1.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point3)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.TextCentered = False
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject1 = sketchRapidDimensionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId4, None)
    
    theSession.SetUndoMarkName(markId3, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId3, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines9 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines12)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId5, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits27 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits37 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits39 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits41 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits45 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    expression3 = workPart.Expressions.FindObject("p0")
    expression3.SetFormula("60")
    
    theSession.SetUndoMarkVisibility(markId5, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(1.1040565590340174)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId6, None)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId5, "Edit Driving Value")
    
    point1_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc2, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    point1_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc2, workPart.ModelingViews.WorkView, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    dimensionlinearunits47 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point4 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point4
    assocOrigin2.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.DimensionLine = 0
    assocOrigin2.AssociatedView = NXOpen.View.Null
    assocOrigin2.AssociatedPoint = NXOpen.Point.Null
    assocOrigin2.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.XOffsetFactor = 0.0
    assocOrigin2.YOffsetFactor = 0.0
    assocOrigin2.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder2.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point5 = NXOpen.Point3d(17.699266136372639, 10.324571912884007, 0.0)
    sketchRapidDimensionBuilder2.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point5)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.TextCentered = False
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject2 = sketchRapidDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId8, None)
    
    theSession.SetUndoMarkName(markId7, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId7, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder3 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines13 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines16)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId9, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits53 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    expression4 = workPart.Expressions.FindObject("p1")
    expression4.SetFormula("20")
    
    theSession.SetUndoMarkVisibility(markId9, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId10, None)
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId9, "Edit Driving Value")
    
    sketchRapidDimensionBuilder3.Destroy()
    
    theSession.UndoToMark(markId11, None)
    
    theSession.DeleteUndoMark(markId11, None)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.86962263904675063
    rotMatrix1.Xy = 0.10795063882299036
    rotMatrix1.Xz = -0.48177082231603924
    rotMatrix1.Yx = 0.47735595024581773
    rotMatrix1.Yy = 0.065283138283980885
    rotMatrix1.Yz = 0.87628158066953932
    rotMatrix1.Zx = 0.12604666763654201
    rotMatrix1.Zy = -0.99201046941728521
    rotMatrix1.Zz = 0.005240815224777793
    translation1 = NXOpen.Point3d(-0.95129519244414684, 9.8204494990815956, 11.34727517388265)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.89692984317447444)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit1 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("70")
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId12, "拉伸 對話方塊")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 2 
    curves1[0] = arc2
    curves1[1] = arc1
    seedPoint1 = NXOpen.Point3d(8.3333333333332362, 11.993587371177549, 0.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(theSession.ActiveSketch, curves1, seedPoint1, 0.01)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId15, None)
    
    direction1 = workPart.Directions.CreateDirection(theSession.ActiveSketch, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction1
    
    unit2 = extrudeBuilder1.Offset.StartOffset.Units
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.DeleteUndoMark(markId14, None)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.9563876666803921
    rotMatrix2.Xy = -0.2913450206238366
    rotMatrix2.Xz = 0.020993093610327536
    rotMatrix2.Yx = 0.29148888998715317
    rotMatrix2.Yy = 0.95656548521648033
    rotMatrix2.Yz = -0.0040865029813069234
    rotMatrix2.Zx = -0.018890686480189961
    rotMatrix2.Zy = 0.010027534605045116
    rotMatrix2.Zz = 0.99977126909811265
    translation2 = NXOpen.Point3d(-14.068184679511843, 30.614735452558271, -34.880454720099529)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.89692984317447444)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.059993953280268852
    rotMatrix3.Xy = -0.9980891490492968
    rotMatrix3.Xz = 0.014791082443673973
    rotMatrix3.Yx = 0.97829614890515826
    rotMatrix3.Yy = 0.061735516783642343
    rotMatrix3.Yz = 0.19780134227247878
    rotMatrix3.Zx = -0.19833650850799769
    rotMatrix3.Zy = 0.0026031745057153652
    rotMatrix3.Zz = 0.98013052848860294
    translation3 = NXOpen.Point3d(-3.3702015740657263, 32.391520507508588, -33.669712178125842)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.89692984317447444)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("30")
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = -0.26634935400322413
    rotMatrix4.Xy = -0.8784760924763424
    rotMatrix4.Xz = -0.3966582616933137
    rotMatrix4.Yx = -0.2724763432735019
    rotMatrix4.Yy = -0.32611598573522216
    rotMatrix4.Yz = 0.90520992383217069
    rotMatrix4.Zx = -0.92456187677102952
    rotMatrix4.Zy = 0.34918207112542443
    rotMatrix4.Zz = -0.15250317120044657
    translation4 = NXOpen.Point3d(10.418473916692285, 15.228186411601804, 3.6659599307200246)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.89692984317447444)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.97787358731533502
    rotMatrix5.Xy = 0.1998732167848099
    rotMatrix5.Xz = 0.061757140827054219
    rotMatrix5.Yx = -0.20690964501052617
    rotMatrix5.Yy = 0.96761042797884345
    rotMatrix5.Yz = 0.14463214880591749
    rotMatrix5.Zx = -0.030848760634078376
    rotMatrix5.Zy = -0.15421010627935844
    rotMatrix5.Zz = 0.98755637666345319
    translation5 = NXOpen.Point3d(-21.317707985083516, 26.491068619492509, -32.494497598341617)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.89692984317447444)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId16, None)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    feature1 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.SetUndoMarkName(markId12, "拉伸")
    
    expression8 = extrudeBuilder1.Limits.StartExtend.Value
    expression9 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression5)
    
    workPart.Expressions.Delete(expression6)
    
    workPart.Expressions.Delete(expression7)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = -0.1310069789365341
    rotMatrix6.Xy = -0.35873205190646579
    rotMatrix6.Xz = -0.92420153992778975
    rotMatrix6.Yx = 0.024379640066352862
    rotMatrix6.Yy = 0.93078837799751224
    rotMatrix6.Yz = -0.36474460727335417
    rotMatrix6.Zx = 0.99108163368118252
    rotMatrix6.Zy = -0.070315789974483719
    rotMatrix6.Zz = -0.11319401512494875
    translation6 = NXOpen.Point3d(-6.5283277737608536, 34.131719960681586, -15.983241721515597)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.89692984317447444)
    
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()