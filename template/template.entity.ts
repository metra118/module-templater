import { Column, Entity, PrimaryColumn } from 'typeorm';

@Entity()
export class TEMPLATEEntity {
  @PrimaryColumn('uuid')
  versionId: string;

  @Column('text')
  title: string;
}
